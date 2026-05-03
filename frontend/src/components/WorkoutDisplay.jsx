export default function WorkoutDisplay({ workout }) {
  if (!workout?.exercises) return null;

  return (
    <div className="workout">
      <h2>Your Workout</h2>

      {workout.exercises.map((ex, i) => (
        <div key={i} className="exercise">
          <h3>{ex.exercise_name}</h3>
          <p><b>Sets:</b> {ex.number_of_sets}</p>
          <p>{ex.how_to_perform}</p>
          <p><b>Form:</b> {ex.key_form}</p>
          <p><b>Safety:</b> {ex.caution_tips}</p>
        </div>
      ))}
    </div>
  );
}
