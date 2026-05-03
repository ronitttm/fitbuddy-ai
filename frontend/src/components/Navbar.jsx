import React, { useState } from "react";
import "./Navbar.css";
import logo from "../assets/logo.png"

export default function Navbar() {
  const [open, setOpen] = useState(false);

  return (
    <nav className="navbar">
      {/* LEFT LOGO */}
      <div className="nav-left">
        <img
          src={logo}
          alt="FitBuddy AI"
          className="logo"
        />
      </div>

      {/* CENTER TITLE */}
      <div className="nav-center">FitBuddy AI</div>

      {/* RIGHT HAMBURGER */}
      <div className="nav-right" onClick={() => setOpen(!open)}>
        <div className={`hamburger ${open ? "open" : ""}`}>
          <span />
          <span />
          <span />
        </div>
      </div>

      {/* MOBILE MENU */}
      {open && (
        <div className="mobile-menu">
          <a href="#">Home</a>
          <a href="#">Workout Generator</a>
          <a href="#">Progress</a>
          <a href="#">About</a>
        </div>
      )}
    </nav>
  );
}
