const express = require('express');
const cors = require('cors');
const app = express();
const { spawn } = require('child_process');
const bodyParser = require('body-parser')

app.use(cors());

var jsonParser = bodyParser.json()

app.post('/createPrediction', jsonParser, async (req, res) => {
    console.log("calculating...");

    const user = req.body;
    var script = "";

    if (user.algorithm === "0") {
        script = "../scripts/knn.py";
    }
    if (user.algorithm === "1") {
        script = "../scripts/svm.py";
    }
    if (user.algorithm === "2") {
        script = "../scripts/nn.py";
    }

    const childPython = spawn('python', [
        script,
        user.age,
        user.sex,
        user.cp,
        user.trestbps,
        user.chol,
        user.fbs,
        user.restecg,
        user.thalach,
        user.exang,
        user.oldpeak,
        user.slope,
        user.ca,
        user.thal
    ]);

    childPython.stdout.on('data', (data) => {
        console.log(`${data}`);
        res.send(`${data}`);
    });

    childPython.stderr.on('data', (data) => {
        console.error(`${data}`);
    });

    console.log("done!");
});

app.listen(3001, () => {
    console.log("running...");
});