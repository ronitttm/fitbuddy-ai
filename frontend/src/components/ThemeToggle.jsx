export default function ThemeToggle({ darkMode, toggle }) {
  return (
    <button className="theme-toggle" onClick={toggle}>
      {darkMode ? "🌙 Dark Mode" :  "☀ Light Mode"}
    </button>
  );
}
