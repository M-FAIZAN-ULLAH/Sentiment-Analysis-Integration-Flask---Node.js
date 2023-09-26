const express = require('express');
const axios = require('axios');

const app = express();
app.use(express.json());

app.post('/analyze', (req, res) => {
    const text = req.body.text;

    axios.post('http://127.0.0.1:5000/analyze', { text })

        .then(response => {
            const result = response.data;
            res.json(result);
            console.log("successfull!")
        })
        .catch(error => {
            console.error(error);
            res.status(500).json({ error: 'An error occurred' });
        });
});

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
