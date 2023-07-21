const express = require('express');
const cors = require('cors');
const axios = require('axios');

if(process.env.NODE_ENV === 'development'){
    const dotenv = require('dotenv');
    dotenv.config();
}

const app = express();
app.use(cors());

// to bypass CORS
app.get('/', async (req, res)=>{
    if(req.query.url){
        //query string with key of url is assume
        console.log(`processing request to ${req.query.url}`)
        const proxyRes = await axios.get(`${req.query.url}&apikey=${process.env.API_KEY}`);
        res.send(proxyRes.data);
    } else {
        res.send('Please provide a url query param')
    }
});

app.listen(process.env.PORT || 5001, ()=> {
    console.log('Listening on port 5001 ....')
})