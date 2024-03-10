import React, { useState, useEffect } from "react";
import SearchTextList from "./components/SearchTextList";
import PriceHistoryTable from "./components/PriceHistoryTable";
import axios from "axios";
import TrackedProductList from "./components/TrackedProductList";
import AmmoList from "./components/AmmoList";

const URL = "http://localhost:5000";

function App() {
  const [showPriceHistory, setShowPriceHistory] = useState(false);
  const [priceHistory, setPriceHistory] = useState([]);
  const [searchTexts, setSearchTexts] = useState([]);
  const [newSearchText, setNewSearchText] = useState("");

  const handleNewSearchTextChange = (event) => {
    setNewSearchText(event.target.value);
  };

  const addonSubmit = async (event) => {
    event.preventDefault();
    try {
      await axios.post(`${URL}/add-scraper`, {
        url: newSearchText
      });
      alert("Scraper adding");
    } catch (error) {
      alert("Error starting scraper:", error);
    }
  };

  const scrapeAll = async (event) => {
    event.preventDefault();
    try {
      await axios.post(`${URL}/start-scrape-all`,{});
      alert("SCRAPING STARTED");
    } catch (error) {
      alert("Error starting scraper:", error);
    }    
  };

  return (
    <div className="main">
      <h1>Ammo Data Tool</h1>
      <form onSubmit={addonSubmit}>
        <label>Add a new item:</label>
        <input
          type="text"
          value={newSearchText}
          onChange={handleNewSearchTextChange}
        />
        <button type="submit">Start Scraper</button>
      </form>
      <form onSubmit={scrapeAll}>
        <label>Start the scraper:  </label>
        <button type="submit">Start</button>
      </form>
      <AmmoList/>
    </div>
  );
}

export default App;
