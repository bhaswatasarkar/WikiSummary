// import axios from 'axios'
function fun(){
    axios.post('/summary',{
        data: 'abc'}).then((response)=>{
            console.log(response);
        },(error)=>{
            console.log(error)
        })
}

// document.getElementById("inputform").addEventListener('submit',(event)=>event.preventDefault())