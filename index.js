    const express = require("express");//express provides easy way to establish web server connection

    const body_parser = require("body-parser"); // parses th req into the readable form from which you can easily extract information
    const axios = require("axios");

    const app = express().use(body_parser.json());
    app.use(express.json({ extended: false }));


    const mysql =  require('mysql2');

    require('dotenv').config();

    // const fs = require('fs'); //file system for logging
    // const logFile = fs.createWriteStream('webhook.log', { flags: 'a' });


    const log4js = require('log4js');
    log4js.configure({
        appenders: {Webhook : {type : 'file', filename : "Webhook.log"}},
        categories :{default : {appenders : ['Webhook'], level : 'info'}}
    });

    const logger = log4js.getLogger("Webhook");


    // db 
    const db = mysql.createConnection({
        host : 'localhost',
        user : 'user', 
        password : 'redhat',
        database : 'webhook'
    });

    db.connect(err =>{
        if (err) {
            logger.error("Database Connection error :",err);
            throw err;
        } else {
            logger.info("Connected to the database");
        }
    });



    //you need to put the callback url on the server eg whatsapp api and verify token that you have set here in env
    //the callback url has been made using ngrok so puth that url + webhoook // endpoint 


    const token = process.env.TOKEN; // for sending the request  // temporary access token
    const mytoken = process.env.MYTOKEN; // for verifiication the webhook


    app.listen(8000 || process.env.PORT,()=>{

        console.log("webhook is listening");

    });

    //  GET https://c986-27-107-168-78.ngrok-free.app/webhook?hub.mode=subscribe&hub.challenge=testchallenge&verify_token=pratik
    // output testchallenge 

    //to verify the callback url from the cloud api side 
    app.get("/webhook",(req,res)=>{

        let mode = req.query["hub.mode"];
        let challenge = req.query["hub.challenge"];
        let verify_token = req.query["verify_token"];


        if(mode && verify_token){

            if (mode === "subscribe" && verify_token === mytoken)
            {
                res.status(200).send(challenge);
                
            }
            else {
                res.status(403).send("Forbidden");
            }
        }

    });



    //this endpoint post/webhoook recived post requ from whatsapp api whenever an event occur in this 
    // its when a customer send a message 
    // the data is logged 
    //it then send the message im pratik back to the user 



    app.post("/webhook", (req, res) => {
        console.log("Webhook hit!"); // working
    
        let body_param = req.body;
    
        console.log(JSON.stringify(body_param, null, 2));
        logger.info('Received Data: ', JSON.stringify(body_param, null, 2));
    
        if (body_param.object) {
            if (body_param.entry &&
                body_param.entry[0].changes &&
                body_param.entry[0].changes[0].value.messages &&
                body_param.entry[0].changes[0].value.messages[0]) {
    
                const phone_number_id = body_param.entry[0].changes[0].value.metadata.phone_number_id;
                const from_phone = body_param.entry[0].changes[0].value.messages[0].from; // user phone number 
                const message_body = body_param.entry[0].changes[0].value.messages[0].text.body;
    
                const dataToInsert = [phone_number_id,from_phone,message_body];    
                   
    
                const query = `insert into webhook_data (phone_number_id,from_phone,message_body)
                values (?,?,?)`;
    
                db.query(query, dataToInsert, (err, result) => {
                    if (err) {  
                        logger.error("Error inserting into database", err);
                    if (!res.headersSent) {
                            return res.status(500).json({ status: "error", message: "Database Error" });
                        }
                    } else {
                        logger.info("Data successfully inserted into the database", result);
                        res.status(200).json({ status: "success" });
                        if (!res.headersSent) {
                        }
                    }
                });
            } else {
                if (!res.headersSent) {
                    res.sendStatus(404);
                }
            }
        } else if (body_param.data) {
            if (!res.headersSent) {
                res.status(200).send(`Received the data ${body_param.data}`);
            }
        } else {
            if (!res.headersSent) {
                res.status(400).send(`Unknown Payload Structure`);
            }
        }
    });
    
        // app.post("/webhook",(req,res)=>{
        //     console.log(JSON.stringify(body_param,null,2));
        //                         res.sendStatus(200);

        // })
 

    //health check
    //A simple endpoint that returns a status message to confirm that the server is up and running.
    app.get("/",(req,res)=>{
        res.status(200).send("hello this is the webhook setup");
    });