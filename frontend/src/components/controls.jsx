export default function Controls({
  setWeightType,
  setFitnessLevel,
  generate,
  loading,
}) {
  return (
    <div className="controls">
      <select onChange={(e) => setWeightType(e.target.value)}>
        <option value="">Equipment</option>
        <option value="dumbbell">Dumbbell</option>
        <option value="barbell">Barbell</option>
        <option value="kettlebell">Kettlebell</option>
        <option value="body-weight">Body Weight</option>
        <option value="machine-assisted">Machine Assisted</option>
      </select>

      <select onChange={(e) => setFitnessLevel(e.target.value)}>
        <option value="">Fitness level</option>
        <option value="beginner">Beginner</option>
        <option value="intermediate">Intermediate</option>
        <option value="advanced">Advanced</option>
      </select>

      <button onClick={generate}>
        {loading ? "Generating..." : "Generate Workout"}
      </button>
    </div>
  );
}
