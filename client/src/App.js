import './App.css';
import { useState, useEffect } from "react";
import Axios from "axios";

function App() {
  const [algorithm, setAlgorithm] = useState(0);
  const [age, setAge] = useState(0);
  const [sex, setSex] = useState(0);
  const [cp, setCp] = useState(0);
  const [trestbps, setTrestbps] = useState(0);
  const [chol, setChol] = useState(0);
  const [fbs, setFbs] = useState(0);
  const [restecg, setRestecg] = useState(0);
  const [thalach, setThalach] = useState(0);
  const [exang, setExang] = useState(0);
  const [oldpeak, setOldpeak] = useState(0);
  const [slope, setSlope] = useState(0);
  const [ca, setCa] = useState(0);
  const [thal, setThal] = useState(0);
  const [prediction, setPrediction] = useState("(blank)");

  useEffect(() => {
  }, []);

  const predictUser = () => {
    setPrediction("Calculating Prediction...");
    Axios.post("http://localhost:3001/createPrediction", {
      algorithm,
      age,
      sex,
      cp,
      trestbps,
      chol,
      fbs,
      restecg,
      thalach,
      exang,
      oldpeak,
      slope,
      ca,
      thal
    }).then((response) => {
      setPrediction(response.data);
    });
  };

  return (
    <div className="app">

      <div className='header'>
        <img className='header_logo' src='https://www.iconpacks.net/icons/1/free-heart-icon-431-thumb.png' alt='' />
        <h1>Heart Disease Predictor</h1>
      </div>

      <div className='form'>
        <h4>Machine Learning Algorithm (0 = k-nearest neighbors, 1 = support vector machine, 2 = neural networks):</h4>
        <input className='textbox' type='number' placeholder='' onChange={(event) => { setAlgorithm(event.target.value) }} />

        <h4>Age in years:</h4>
        <input className='textbox' type='number' placeholder='' onChange={(event) => { setAge(event.target.value) }} />
        
        <h4>Sex (1 = male; 0 = female):</h4>
        <input className='textbox' type='number' placeholder='' onChange={(event) => { setSex(event.target.value) }} />
        
        <h4>Chest pain type (1 = typical angina, 2 = atypical angina, 3 = non-anginal pain, 4 = asymptomatic):</h4>
        <input className='textbox' type='number' placeholder='' onChange={(event) => { setCp(event.target.value) }} />
        
        <h4>Resting blood pressure:</h4>
        <input className='textbox' type='number' placeholder='' onChange={(event) => { setTrestbps(event.target.value) }} />
        
        <h4>Serum cholestoral:</h4>
        <input className='textbox' type='number' placeholder='' onChange={(event) => { setChol(event.target.value) }} />
        
        <h4>Fasting blood sugar > 120 mg/dl (1 = true; 0 = false):</h4>
        <input className='textbox' type='number' placeholder='' onChange={(event) => { setFbs(event.target.value) }} />
        
        <h4>Resting electrocardiographic results ( 0 = normal, 1 = having ST-T wave abnormality, 2 = showing probable or definite left ventricular hypertrophy by Estes criteria):</h4>
        <input className='textbox' type='number' placeholder='' onChange={(event) => { setRestecg(event.target.value) }} />
        
        <h4>Maximum heart rate achieved:</h4>
        <input className='textbox' type='number' placeholder='' onChange={(event) => { setThalach(event.target.value) }} />
        
        <h4>Exercise induced angina (1 = yes, 0 = no):</h4>
        <input className='textbox' type='number' placeholder='' onChange={(event) => { setExang(event.target.value) }} />
        
        <h4>ST depression induced by exercise relative to rest:</h4>
        <input className='textbox' type='number' placeholder='' onChange={(event) => { setOldpeak(event.target.value) }} />
        
        <h4>The slope of the peak exercise ST segment (1 = upsloping, 2 = flat, 3 = downsloping):</h4>
        <input className='textbox' type='number' placeholder='' onChange={(event) => { setSlope(event.target.value) }} />
        
        <h4>Number of major vessels (0-3) colored by flourosopy:</h4>
        <input className='textbox' type='number' placeholder='' onChange={(event) => { setCa(event.target.value) }} />
        
        <h4>Thal (3 = normal, 6 = fixed defect, 7 = reversable defect):</h4>
        <input className='textbox' type='number' placeholder='' onChange={(event) => { setThal(event.target.value) }} />
        
        <div className='button-border'>
          <button className='button' onClick={predictUser}> Predict </button>
        </div>
      </div>

      <div className='footer'>
        <h1>Prediction = {prediction}</h1>
      </div>

    </div>
  );
}

export default App;
