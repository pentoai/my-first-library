import { useState } from "react";
import "./App.css";

function App() {
  const [error, setError] = useState<string | null>(null);

  return (
    <div className="app">
      <header className="header">
        <h1>Library Management</h1>
      </header>

      {error && (
        <div className="error-banner">
          <span>{error}</span>
          <button onClick={() => setError(null)}>&times;</button>
        </div>
      )}

      <main className="content">
        {/* Add your components here */}
        <p>Your Library App Goes Here!</p>
      </main>
    </div>
  );
}

export default App;
