export default function SelectedMuscles({ selectedMuscles, removeMuscle }) {
  if (!selectedMuscles.length) return null;

  return (
    <div style={{ marginTop: 20, textAlign: "center" }}>
      <h3>Selected muscles</h3>

      <div style={{ display: "flex", gap: 10, flexWrap: "wrap", justifyContent: "center" }}>
        {selectedMuscles.map((muscle) => (
          <span
            key={muscle}
            onClick={() => removeMuscle(muscle)}
            style={{
              padding: "6px 12px",
              background: "#ff4757",
              color: "#fff",
              borderRadius: "20px",
              fontSize: 13,
              cursor: "pointer",
            }}
          >
            {muscle.replace("-", " ")}
          </span>
        ))}
      </div>
    </div>
  );
}
