import React, { useState, useEffect } from 'react';
import AmmoRow from "./AmmoRow.jsx"
import axios from "axios";
const URL = "http://localhost:5000";


function AmmoList() {
  const [handgunAmmo, setHandgunAmmo] = useState([]);
  const [rifleAmmo, setRifleAmmo] = useState([]);
  const [rimfireAmmo, setRimfireAmmo] = useState([]);
  const [shotgunAmmo, setShotgunAmmo] = useState([]);
  useEffect(()=> {
    showHandgunInventory();
    showRifleInventory();
    showRimfireInventory();
    showShotgunInventory();
  }, [])
  const showHandgunInventory = async () => {
    try {
      const response = await axios.get(`${URL}/results?type=1`);
      const data = response.data;
      setHandgunAmmo(data);
    } catch (error) {
      alert("Error getting data:", error);
    }
  }
  const showRifleInventory = async () => {
    try {
      const response = await axios.get(`${URL}/results?type=2`);
      const data = response.data;
      setRifleAmmo(data);
    } catch (error) {
      alert("Error getting data:", error);
    }
  }
  const showRimfireInventory = async () => {
    try {
      const response = await axios.get(`${URL}/results?type=3`);
      const data = response.data;
      setRimfireAmmo(data);
    } catch (error) {
      alert("Error getting data:", error);
    }
  }
  const showShotgunInventory = async () => {
    try {
      const response = await axios.get(`${URL}/results?type=4`);
      const data = response.data;
      setShotgunAmmo(data);
    } catch (error) {
      alert("Error getting data:", error);
    }
  }
  return (
    <div>
      <h2>Handgun Ammos</h2>
      <form onSubmit={showHandgunInventory}>
        <label>Grab all data:</label>
        <button type="submit">Load Data</button>
      </form>
      <table>
        <thead>
        <tr>
          <th>Name</th>
          <th>Price</th>
          <th>Quantity</th>
          <th>Last Updated</th>
          <th>Update</th>
        </tr>
        </thead>
        <tbody>
        {handgunAmmo.map((ammo, index) => (
          <AmmoRow key={index}
            ammoRow={ammo}
          />
        ))}
        </tbody>
      </table>
      <h2>Rifle Ammos</h2>
      <form onSubmit={showRifleInventory}>
        <label>Grab all data:</label>
        <button type="submit">Load Data</button>
      </form>
      <table>
        <thead>
        <tr>
          <th>Name</th>
          <th>Price</th>
          <th>Quantity</th>
          <th>Last Updated</th>
          <th>Update</th>
        </tr>
        </thead>
        <tbody>
        {rifleAmmo.map((ammo, index) => (
          <AmmoRow key={index}
            ammoRow={ammo}
          />
        ))}
        </tbody>
      </table>
      <h2>Rimfire Ammos</h2>
      <form onSubmit={showRimfireInventory}>
        <label>Grab all data:</label>
        <button type="submit">Load Data</button>
      </form>
      <table>
        <thead>
        <tr>
          <th>Name</th>
          <th>Price</th>
          <th>Quantity</th>
          <th>Last Updated</th>
          <th>Update</th>
        </tr>
        </thead>
        <tbody>
        {rimfireAmmo.map((ammo, index) => (
          <AmmoRow key={index}
            ammoRow={ammo}
          />
        ))}
        </tbody>
      </table>
      <h2>Shotgun Ammos</h2>
      <form onSubmit={showShotgunInventory}>
        <label>Grab all data:</label>
        <button type="submit">Load Data</button>
      </form>
      <table>
        <thead>
        <tr>
          <th>Name</th>
          <th>Price</th>
          <th>Quantity</th>
          <th>Last Updated</th>
          <th>Update</th>
        </tr>
        </thead>
        <tbody>
        {shotgunAmmo.map((ammo, index) => (
          <AmmoRow key={index}
            ammoRow={ammo}
          />
        ))}
        </tbody>
      </table>
    </div>
  );
}

export default AmmoList;
