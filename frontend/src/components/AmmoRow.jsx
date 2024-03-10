import React, { useState, useEffect } from 'react';
import axios from "axios";
import AmmoList from "./AmmoList"

function AmmoRow({ ammoRow }) {

  async function updateRow() {
    try {
      await axios.post(`http://localhost:5000/start-scraper`, {
        url: ammoRow.url,
        id: ammoRow.id
      });
    } catch (error) {
      alert("Error update data:", error);
    }
  };
  return (
    <tr>
        <td>{ammoRow.name}</td>
        <td>{ammoRow.price}</td>
        <td>{ammoRow.quantity}</td>
        <td>{ammoRow.created_at}</td>
        <td><button onClick={updateRow}>Update</button></td>
    </tr>

  );
}

export default AmmoRow;
