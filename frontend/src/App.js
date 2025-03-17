import React, { useState, useEffect } from 'react';

function App() {
  const [data, setData] = useState({});

  useEffect(() => {
    fetch('/api/data')
      .then(res => res.json())
      .then(data => setData(data));
  }, []);

  return (
    <div>
      <h1>Frontend</h1>
      <p>Data from backend: {data.name} - {data.value}</p>
    </div>
  );
}

export default App;