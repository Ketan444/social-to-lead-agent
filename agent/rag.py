import json

def load_knowledge():
    with open("data/autostream_knowledge.json", "r") as f:
        return json.load(f)

def answer_from_knowledge(question: str) -> str:
    q = question.lower()

    if "basic" in q:
        return "The Basic plan costs $29 per month and includes 10 videos per month at 720p resolution."

    if "pro" in q:
        return "The Pro plan costs $79 per month and includes unlimited videos, 4K resolution, AI captions, and priority support."

    if "refund" in q:
        return "AutoStream does not offer refunds after 7 days."

    if "support" in q:
        return "24/7 support is available only for Pro plan users."

    return "I can help with pricing, plans, or features. What would you like to know?"
