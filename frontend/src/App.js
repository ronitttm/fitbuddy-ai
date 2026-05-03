import React, { useState } from "react";
import "./App.css";

import BodySelector from "./components/BodySelector";
import SelectedMuscles from "./components/SelectedMuscle";
import Controls from "./components/controls";
import WorkoutDisplay from "./components/WorkoutDisplay";
import ThemeToggle from "./components/ThemeToggle";
import Navbar from "./components/Navbar";

import { generateWorkout } from "./api/workout";

function App() {
  const [darkMode, setDarkMode] = useState(false);
  const [selectedMuscles, setSelectedMuscles] = useState([]);
  const [weightType, setWeightType] = useState("");
  const [fitnessLevel, setFitnessLevel] = useState("");
  const [workout, setWorkout] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleMuscleClick = ({ muscle }) => {
    setSelectedMuscles((prev) =>
      prev.includes(muscle)
        ? prev.filter((m) => m !== muscle)
        : [...prev, muscle]
    );
  };

  const generate = async () => {
    if (!selectedMuscles.length) return alert("Select muscles first");
    if (!weightType || !fitnessLevel) return alert("Select equipment & level");

    setLoading(true);

    const result = await generateWorkout({
      target_muscle: selectedMuscles,
      weight_type: weightType,
      fitness_level: fitnessLevel,
    });

    setWorkout(result);
    setLoading(false);
  };

  return (
    <div className={darkMode ? "App" : "App dark"}>
      <Navbar/>

      <ThemeToggle
        darkMode={darkMode}
        toggle={() => setDarkMode(!darkMode)}
      />

      <BodySelector
        selectedMuscles={selectedMuscles}
        onMuscleClick={handleMuscleClick}
      />

      <SelectedMuscles
        selectedMuscles={selectedMuscles}
        removeMuscle={(m) =>
          setSelectedMuscles(selectedMuscles.filter((x) => x !== m))
        }
      />

      <Controls
        setWeightType={setWeightType}
        setFitnessLevel={setFitnessLevel}
        generate={generate}
        loading={loading}
      />

      <WorkoutDisplay workout={workout} />
    </div>
  );
}

export default App;
