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
  const [prediction, setPrediction] = useState("");

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
    <div className="App">

      <div className='Header'>
        <h1>Heart Disease Predictor</h1>
      </div>

      <div className='Inputs'>
        <input type='number' placeholder='ml algorithm 0 = knn, 1 = svm, 2 = nn' onChange={(event) => { setAlgorithm(event.target.value) }} />
        <input type='number' placeholder='age in years' onChange={(event) => { setAge(event.target.value) }} />
        <input type='number' placeholder='sex (1 = male; 0 = female)' onChange={(event) => { setSex(event.target.value) }} />
        <input type='number' placeholder='chest pain type -- Value 1: typical angina -- Value 2: atypical angina -- Value 3: non-anginal pain -- Value 4: asymptomatic' onChange={(event) => { setCp(event.target.value) }} />
        <input type='number' placeholder='resting blood pressure' onChange={(event) => { setTrestbps(event.target.value) }} />
        <input type='number' placeholder='serum cholestoral' onChange={(event) => { setChol(event.target.value) }} />
        <input type='number' placeholder='(fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)' onChange={(event) => { setFbs(event.target.value) }} />
        <input type='number' placeholder='resting electrocardiographic results -- Value 0: normal -- Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV) -- Value 2: showing probable or definite left ventricular hypertrophy by Estes criteria' onChange={(event) => { setRestecg(event.target.value) }} />
        <input type='number' placeholder='maximum heart rate achieved' onChange={(event) => { setThalach(event.target.value) }} />
        <input type='number' placeholder='exercise induced angina (1 = yes; 0 = no)' onChange={(event) => { setExang(event.target.value) }} />
        <input type='number' placeholder='ST depression induced by exercise relative to rest' onChange={(event) => { setOldpeak(event.target.value) }} />
        <input type='number' placeholder='the slope of the peak exercise ST segment -- Value 1: upsloping -- Value 2: flat -- Value 3: downsloping' onChange={(event) => { setSlope(event.target.value) }} />
        <input type='number' placeholder='number of major vessels (0-3) colored by flourosopy' onChange={(event) => { setCa(event.target.value) }} />
        <input type='number' placeholder='thal: 3 = normal; 6 = fixed defect; 7 = reversable defect' onChange={(event) => { setThal(event.target.value) }} />
        <button onClick={predictUser}> Predict </button>
      </div>

      <div className='Header'>
        <h1>Prediction = {prediction}</h1>
      </div>

    </div>
  );
}

export default App;
