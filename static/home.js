
// document.getElementById("inputform").addEventListener('submit',(event)=>event.preventDefault())

document.getElementById("radio-word-count").addEventListener('change',wordCount)

function wordCount(e){
    console.log(e)
    if (this.checked) {
        document.getElementById('word-count-data').innerHTML = `<div class="input-group input-group-sm mb-3">
        <span class="input-group-text" id="inputGroup-sizing-sm">Enter number of words</span>
        <input type="text" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-sm" name="wordCount">
      </div>`;
    }
    else{
        document.getElementById('word-count-data').innerHTML = ``;
    }
}




document.getElementById("radio-ratio-value").addEventListener('change',ratioValue)

function ratioValue(e){
    console.log(e)
    if (this.checked) {
        document.getElementById('ratio-value-data').innerHTML = `<div class="input-group input-group-sm mb-3">
        <span class="input-group-text" id="inputGroup-sizing-sm">Enter ratio value(%)</span>
        <input type="text" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-sm" name="ratioValue">
      </div>`;
    }
    else{
        document.getElementById('ratio-value-data').innerHTML = ``;
    }
}



document.getElementById("radio-sentence-count").addEventListener('change',sentenceCount)

function sentenceCount(e){
    console.log(e)
    if (this.checked) {
        document.getElementById('sentence-count-data').innerHTML = `<div class="input-group input-group-sm mb-3">
        <span class="input-group-text" id="inputGroup-sizing-sm">Enter number of sentences</span>
        <input type="text" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-sm" name="sentenceCount">
      </div>`;
    }
    else{
        document.getElementById('sentence-count-data').innerHTML = ``;
    }
}



// document.addEventListener('DOMContentLoaded', function(event) { 
//     document.getElementById('basic-url').value = 'bar';
// })