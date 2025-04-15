from flask import Flask, jsonify, request, render_template, url_for
import requests

app = Flask(__name__)

# In-memory storage for meme votes
vote_stats = {}

# 📥 Get 1 or more memes
def get_memes(subreddit=None, count=1):
    base_url = "https://meme-api.com/gimme"
    url = f"{base_url}/{subreddit}/{count}" if subreddit else f"{base_url}/{count}"
    response = requests.get(url).json()

    # If only one meme is returned, it's a dict. If multiple, it's in response["memes"]
    memes = response["memes"] if "memes" in response else [response]

    result = []
    for meme in memes:
        meme_data = {
            "id": meme["postLink"],  # Using postLink as a unique ID
            "title": meme["title"],
            "meme_url": meme["url"],
            "subreddit": meme["subreddit"],
            "post_link": meme["postLink"],
            "author": meme["author"],
            "nsfw": meme["nsfw"],
            "spoiler": meme["spoiler"],
            "upvotes": vote_stats.get(meme["postLink"], {}).get("upvotes", 0),
            "downvotes": vote_stats.get(meme["postLink"], {}).get("downvotes", 0)
        }
        result.append(meme_data)
    return result

@app.route("/")
def home():
    return render_template("index.html")

# GET meme(s) with optional count
@app.route("/api/meme", methods=["GET"])
def random_memes():
    count = int(request.args.get("count", 1))
    memes = get_memes(count=count)
    return jsonify(memes)

# GET meme(s) from a subreddit
@app.route("/api/meme/<subreddit>", methods=["GET"])
def subreddit_memes(subreddit):
    count = int(request.args.get("count", 1))
    memes = get_memes(subreddit=subreddit, count=count)
    return jsonify(memes)

# POST vote on a meme
@app.route("/api/meme/vote", methods=["POST"])
def vote_meme():
    data = request.get_json()
    meme_id = data.get("meme_id")
    vote_type = data.get("vote")  # "upvote" or "downvote"

    if not meme_id or vote_type not in ["upvote", "downvote"]:
        return jsonify({"error": "Invalid payload"}), 400

    # Initialize vote stats if this meme hasn't been voted yet
    if meme_id not in vote_stats:
        vote_stats[meme_id] = {"upvotes": 0, "downvotes": 0}

    # Count the vote
    vote_stats[meme_id][f"{vote_type}s"] += 1

    return jsonify({
        "message": f"{vote_type.capitalize()} recorded",
        "votes": vote_stats[meme_id]
    })

if __name__ == "__main__":
    app.run(debug=True)
