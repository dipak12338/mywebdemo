from flask import Flask, request, jsonify
import hmac
import hashlib
import os

app = Flask(__name__)

# Replace this with the secret you set up in GitHub (if any)
WEBHOOK_SECRET = os.getenv('WEBHOOK_SECRET', 'your-webhook-secret')

def verify_signature(payload, signature):
    """Verify the signature of the webhook payload."""
    secret = WEBHOOK_SECRET.encode()
    hash = hmac.new(secret, payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(f'sha256={hash}', signature)

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    """Handle incoming GitHub webhook payloads."""
    signature = request.headers.get('X-Hub-Signature-256')
    
    # Verify signature
    if not verify_signature(request.data, signature):
        return jsonify({'error': 'Invalid signature'}), 400

    # Process the payload
    payload = request.json
    print("Received payload:", payload)

    # Respond to acknowledge receipt
    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)
