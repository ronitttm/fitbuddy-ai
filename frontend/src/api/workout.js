export async function generateWorkout(payload) {
  const res = await fetch('http://127.0.0.1:8000/json-generate', {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });

  return res.json();
}
