const API_URL = "http://127.0.0.1:5000/events";

const list = document.getElementById("event-list");
const form = document.querySelector("form");
const titleInput = document.getElementById("title");

// Add one event to the page
function addEventToList(event) {
  const li = document.createElement("li");
  li.textContent = event.title;
  list.appendChild(li);
}

// GET: load all events when the page opens
async function loadEvents() {
  const response = await fetch(API_URL);
  const events = await response.json();
  list.innerHTML = "";
  events.forEach(addEventToList);
}

// POST: send a new event when the form is submitted
form.addEventListener("submit", async (e) => {
  e.preventDefault(); // stop the page from reloading

  const title = titleInput.value.trim();
  if (!title) return;

  const response = await fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title }),
  });

  if (response.ok) {
    addEventToList(await response.json());
    titleInput.value = "";
  } else {
    alert("Could not add event");
  }
});

loadEvents();