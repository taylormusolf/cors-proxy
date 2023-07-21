const express = require('express');
const cors = require('cors');
const axios = require('axios');

const { Configuration, OpenAIApi } = require("openai");

if(process.env.NODE_ENV === 'development'){
    const dotenv = require('dotenv');
    dotenv.config();
}

const app = express();
app.use(cors());

//python setup



app.get('/python/', (req, res) => {
    let runPy = new Promise(function(success, nosuccess) {

        const { spawn } = require('child_process');
        const pyprog = spawn('python3', ['./python.py'], 'banana');

        pyprog.stdout.on('data', function(data) {

            success(data);
        });

        pyprog.stderr.on('data', (data) => {

            nosuccess(data);
        });
    });
    runPy.then(function(fromRunpy) {
        res.end(fromRunpy);
    });
})





// //CHAT GPT route

app.post('/chat', async (req, res)=>{
    console.log(`processing chat request`)
    const openai = new OpenAIApi(new Configuration({
        apiKey: process.env.CHAT_API_KEY
    }));
    let chat = await openai.createChatCompletion({
        model: "gpt-4",
        // model: "gpt-3.5-turbo",
        messages: req.body.messages,
        max_tokens: 150,
        temperature: 0.9
    });
    return chat.data.choices[0].message

});

// to bypass CORS
app.get('/', async (req, res)=>{


    if(req.query.url){
        //query string with key of url is assume
        console.log(`processing request to ${req.query.url}`)
        const proxyRes = await axios.get(`${req.query.url}`);
        res.send(proxyRes.data);
    } else {
        res.send('Please provide a url query param')
    }
});



app.listen(process.env.PORT || 5002, ()=> {
    console.log('Listening on port 5001 ....')
})