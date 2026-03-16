# CLI Movie Recommender Challenge

## Goal
Build a **command-line movie recommender** that uses a public movie API and your own scoring/ranking logic to recommend the best movies for a user's preferences.

This project is not just about fetching data. Your program must:
- collect user preferences,
- fetch candidate movie data from an API,
- filter unsuitable results,
- score the remaining results,
- rank them,
- and print the best recommendations in the terminal.

---

## Example Usage

```bash
python recommender.py
```

Example session:

```text
Preferred genre: sci-fi
Minimum rating: 7
Earliest year: 2010
Maximum runtime (minutes): 140
How many recommendations? 5

Top recommendations:
1. Arrival (2016) | Rating: 7.9 | Runtime: 116 | Score: 92
2. Ex Machina (2014) | Rating: 7.7 | Runtime: 108 | Score: 88
3. Blade Runner 2049 (2017) | Rating: 8.0 | Runtime: 164 | Score: 74
```

---

## Requirements

### Level 1: Basic API Search
Your program should:
- ask the user for movie preferences,
- fetch movie data from an API,
- show a list of matching movies,
- handle empty/no-result cases cleanly.

**Minimum inputs:**
- genre
- minimum rating
- earliest release year
- maximum runtime
- number of recommendations to show

**Output:**
- movie title
- year
- rating
- runtime

---

### Level 2: Filtering
Before recommending movies, filter out titles that do not match the user’s constraints.

Your program should remove movies that fail any required condition, such as:
- rating too low,
- released too early,
- runtime too long,
- missing important fields.

If too few valid movies remain, print a useful message.

---

### Level 3: Recommendation Algorithm
This is the most important part.

Design a **scoring system** that ranks the remaining movies.

Your algorithm must consider multiple factors, for example:
- rating
- release year
- runtime closeness to the user’s preferred maximum
- genre match quality

You may choose your own scoring formula, but you must:
- explain it briefly in comments or a README note,
- use it consistently,
- sort recommendations from best to worst.

The recommendation quality should come from **your logic**, not just the order returned by the API.

---

### Level 4: Robust CLI Behavior
Your program should also:
- validate user input,
- handle API/network errors gracefully,
- handle missing or incomplete movie data,
- avoid crashing on bad input.

Examples:
- non-numeric rating,
- negative runtime,
- invalid year,
- API timeout,
- empty API response.

---

## Rules
- The project must be **CLI-only**.
- Use a real movie API.
- Do not hardcode the final movie recommendations.
- Do not skip the scoring/ranking step.
- Keep the interface text-based only.

---

## Suggested APIs
Pick one:
- OMDb API
- TMDb API

If an API requires a key, store it safely (for example in an environment variable or config file that is not committed).

---

## Skills Practiced
- API requests
- JSON parsing
- CLI input/output
- filtering and sorting
- ranking algorithms
- error handling
- clean program structure

---

## Deliverables
Your finished project should include:
- `recommender.py`
- clear instructions for how to run it
- a short note describing how your scoring algorithm works

---

## Stretch Ideas
Choose one or more if you finish early:
- support multiple genres
- let users exclude specific genres
- add a “surprise me” mode
- save previous searches to a file
- show why each movie received its score
- let users compare two movies directly

---

## Hint Section
Use these hints only if needed:
- Start by making the API request work first.
- Then print raw movie data.
- After that, add filtering.
- Add scoring only after filtering works.
- Finally, sort and print the top results cleanly.

---

## Success Criteria
A strong submission should:
- use live API data,
- apply meaningful filtering,
- rank results using a clear algorithm,
- produce useful CLI recommendations,
- and handle bad input without crashing.
