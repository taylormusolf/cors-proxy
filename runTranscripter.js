const spawner = require('child_process').spawn;

function extract(data_to_pass_in){

    return new Promise((resolve, reject)  => {
        let script = {};
        const pythonProcess = spawner('python3', ['./transcripter.py', data_to_pass_in]);
        pythonProcess.stdout.on('data', (data) => {
            script.fullText = data.toString();
        });
        
        // on close
        pythonProcess.on('close', (code) => {
            if(code !== 0) {
                return reject(new Error("Python process exited with code " + code));
            }
            resolve(script);
        });

        //! Should have an stderr for error handling
        // pythonProcess.stderr.on('data', (data) => {
        //     reject(new Error(data.toString()));
        // });

    });
};



module.exports = extract;