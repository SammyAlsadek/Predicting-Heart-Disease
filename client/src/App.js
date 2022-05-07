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

        <h4>Machine Learning Algorithm:</h4>
        <form>
          <div>
            <input type='radio' id='knn' name='algo' value='0' onChange={(event) => { setAlgorithm(event.target.value) }} />
            <label for='knn'>K-Nearest Neighbors</label>

            <input type='radio' id='svm' name='algo' value='1' onChange={(event) => { setAlgorithm(event.target.value) }} />
            <label for='svm'>Support Vector Machine</label>

            <input type='radio' id='nn' name='algo' value='2' onChange={(event) => { setAlgorithm(event.target.value) }} />
            <label for='nn'>Neural Networks</label>
          </div>
        </form>

        <h4>Age in years:</h4>
        <input className='textbox' type='number' placeholder='' min='0' onChange={(event) => { event.target.value = Math.abs(event.target.value); setAge(event.target.value) }} />
        
        <h4>Sex:</h4>
        <form>
          <div>
            <input type='radio' id='male' name='sex' value='1' onChange={(event) => { setSex(event.target.value) }} />
            <label for='male'>Male</label>

            <input type='radio' id='female' name='sex' value='0' onChange={(event) => { setSex(event.target.value) }} />
            <label for='female'>Female</label>
          </div>
        </form>
        
        <h4>Chest Pain Type:</h4>
        <form>
          <div>
            <input type='radio' id='ta' name='chest' value='0' onChange={(event) => { setCp(event.target.value) }} />
            <label for='ta'>Typical Angina</label>

            <input type='radio' id='aa' name='chest' value='1' onChange={(event) => { setCp(event.target.value) }} />
            <label for='aa'>Atypical Angina</label>

            <input type='radio' id='nap' name='chest' value='2' onChange={(event) => { setCp(event.target.value) }} />
            <label for='nap'>Non-Anginal Pain</label>

            <input type='radio' id='asymp' name='chest' value='3' onChange={(event) => { setCp(event.target.value) }} />
            <label for='asymp'>Asymptomatic</label>
          </div>
        </form>
        
        <h4>Resting Blood Pressure:</h4>
        <input className='textbox' type='number' placeholder='' min='0' onChange={(event) => { event.target.value = Math.abs(event.target.value); setTrestbps(event.target.value) }} />
        
        <h4>Serum cholestoral:</h4>
        <input className='textbox' type='number' placeholder='' min='0' onChange={(event) => { event.target.value = Math.abs(event.target.value); setChol(event.target.value) }} />
        
        <h4>Fasting blood sugar {'>'} 120 mg/dl:</h4>
        <form>
          <div>
            <input type='radio' id='yes' name='fbs' value='1' onChange={(event) => { setFbs(event.target.value) }} />
            <label for='yes'>Yes</label>

            <input type='radio' id='no' name='fbs' value='0' onChange={(event) => { setFbs(event.target.value) }} />
            <label for='no'>No</label>
          </div>
        </form>
        
        <h4>Resting Electrocardiographic Results:</h4>
        <form>
          <div>
            <input type='radio' id='normal' name='rer' value='0' onChange={(event) => { setRestecg(event.target.value) }} />
            <label for='normal'>Normal</label>

            <input type='radio' id='have' name='rer' value='1' onChange={(event) => { setRestecg(event.target.value) }} />
            <label for='have'>Having ST-T Wave Abnormality</label>

            <input type='radio' id='show' name='rer' value='2' onChange={(event) => { setRestecg(event.target.value) }} />
            <label for='show'>Showing probable or definite left ventricular hypertrophy by Estes criteria</label>
          </div>
        </form>
        
        <h4>Maximum Heart Rate Achieved:</h4>
        <input className='textbox' type='number' placeholder='' min='0' onChange={(event) => { event.target.value = Math.abs(event.target.value); setThalach(event.target.value) }} />
        
        <h4>Exercise Induced Angina:</h4>
        <form>
          <div>
            <input type='radio' id='yes' name='eia' value='1' onChange={(event) => { setExang(event.target.value) }} />
            <label for='yes'>Yes</label>

            <input type='radio' id='no' name='iea' value='0' onChange={(event) => { setExang(event.target.value) }} />
            <label for='no'>No</label>
          </div>
        </form>
        
        <h4>ST depression induced by exercise relative to rest:</h4>
        <input className='textbox' type='number' placeholder='' min='0' onChange={(event) => { event.target.value = Math.abs(event.target.value); setOldpeak(event.target.value) }} />
        
        <h4>The slope of the peak exercise ST segment:</h4>
        <form>
          <div>
            <input type='radio' id='up' name='slope' value='1' onChange={(event) => { setSlope(event.target.value) }} />
            <label for='up'>Upsloping</label>

            <input type='radio' id='flat' name='slope' value='2' onChange={(event) => { setSlope(event.target.value) }} />
            <label for='flat'>Flat</label>

            <input type='radio' id='down' name='slope' value='3' onChange={(event) => { setSlope(event.target.value) }} />
            <label for='down'>Downsloping</label>
          </div>
        </form>

        <h4>Number of major vessels colored by flourosopy:</h4>
        <form>
          <div>
            <input type='radio' id='0' name='ca' value='0' onChange={(event) => { setCa(event.target.value) }} />
            <label for='0'>0</label>

            <input type='radio' id='1' name='ca' value='1' onChange={(event) => { setCa(event.target.value) }} />
            <label for='1'>1</label>

            <input type='radio' id='2' name='ca' value='2' onChange={(event) => { setCa(event.target.value) }} />
            <label for='2'>2</label>

            <input type='radio' id='3' name='ca' value='3' onChange={(event) => { setCa(event.target.value) }} />
            <label for='3'>3</label>
          </div>
        </form>

        <h4>Thal:</h4>
        <form>
          <div>
            <input type='radio' id='normal' name='thal' value='3' onChange={(event) => { setThal(event.target.value) }} />
            <label for='normal'>Normal</label>

            <input type='radio' id='fd' name='thal' value='6' onChange={(event) => { setThal(event.target.value) }} />
            <label for='fd'>Fixed Defect</label>

            <input type='radio' id='rd' name='thal' value='7' onChange={(event) => { setThal(event.target.value) }} />
            <label for='rd'>Reversable Defect</label>
          </div>
        </form>
        
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
