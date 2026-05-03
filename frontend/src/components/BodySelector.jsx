import Body from "react-body-highlighter";
import { ALL_MUSCLES } from "../data/muscles";

export default function BodySelector({ selectedMuscles, onMuscleClick }) {
  const highlighted = ALL_MUSCLES
    .filter((m) => m.muscles.some((x) => selectedMuscles.includes(x)))
    .map((m) => ({ ...m, frequency: 1 }));

  return (
    <div style={{ display: "flex", gap: "40px", justifyContent: "center" }}>
      <div style={{ width: "220px" }}>
        <Body
          type="anterior"
          data={highlighted}
          highlightedColors={["#ff4757"]}
          onClick={onMuscleClick}
        />
      </div>

      <div style={{ width: "220px" }}>
        <Body
          type="posterior"
          data={highlighted}
          highlightedColors={["#ff4757"]}
          onClick={onMuscleClick}
        />
      </div>
    </div>
  );
}
