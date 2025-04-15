# Meme Machine 🔥

A fun and lightweight web app built with **Flask** that fetches random memes from the internet, displays them on a webpage, and lets users upvote/downvote them!

![screenshot](https://user-images.githubusercontent.com/your-placeholder/screenshot.png) <!-- Replace with actual image if you have one -->

## 🚀 Features

- Fetch random memes from [meme-api.com](https://meme-api.com/)
- Vote on memes (upvote/downvote)
- Filter memes by subreddit
- Clean and responsive frontend UI

## 🛠️ Tech Stack

- **Backend:** Python + Flask
- **Frontend:** HTML, CSS, JavaScript
- **External API:** [meme-api.com](https://meme-api.com/)

---

## 📁 Project Structure

```

meme-machine/
│ ├── app.py # Flask app (API + routes)
├── templates/
│ └── index.html # Main frontend page
├── static/
│ └── style.css # Styles for the frontend
├── README.md

```


---

## 🧪 API Endpoints

### `GET /api/meme?count=1`
Returns 1 or more random memes.

**Query Parameters:**
- `count` *(optional)*: number of memes to fetch (default: 1)

---

### `GET /api/meme/<subreddit>?count=1`
Returns memes from a specific subreddit.

**Path Parameter:**
- `subreddit`: name of the subreddit

**Query Parameters:**
- `count` *(optional)*: number of memes (max: 50)

---

### `POST /api/meme/vote`
Registers a vote on a meme.

**Request Body:**
```json
{
  "meme_id": "https://reddit.com/r/memes/abc123",
  "vote": "upvote" // or "downvote"
}
```

## 💻 How to Run
1. **Clone the repo**
```
git clone https://github.com/your-username/meme-machine.git
cd meme-machine
```
2. **Install dependencies**
```
pip install flask requests
```
3. **Run the app**
```
python app.py
```
The app will be available at http://127.0.0.1:5000/.


## 📝 Notes

- Votes are stored in-memory — restarting the app resets them.
- Meme data is fetched live from meme-api.com, so availability depends on that API.

## ✅ What’s Good

1.    **Clear Use of HTTP Methods:**

        GET for retrieving memes.

        POST for voting — aligns well with REST principles.

2.    **Use of Query Parameters and Path Variables:**

        /api/meme?count=5 for query param usage.

        /api/meme/<subreddit> shows path parameter usage.

3.    **Separation of Concerns:**

        The get_memes() function handles meme fetching logic separately from the route handlers.

4.    **Good JSON Responses:**

        Returns well-structured JSON with informative fields.

5.    **In-Memory Data Structure:**

        The vote_stats dictionary is a simple and effective way to simulate state management.

6.    **Basic Input Validation:**

        Checks for valid vote types and meme IDs.
