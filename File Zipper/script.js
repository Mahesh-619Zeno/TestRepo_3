import { HuffmanCoder } from './huffman.js';


onload = function () {
    // Get reference to elements
    const treearea = document.getElementById('treearea');
    const encode = document.getElementById('encode');
    const decode = document.getElementById('decode');
    const temptext = document.getElementById('temptext');
    const upload = document.getElementById('uploadedFile');

    const coder = new HuffmanCoder();

    upload.addEventListener('change',()=>{ alert("File uploaded") });

    encode.onclick = function () {

        const uploadedFile = upload.files[0];
        if(uploadedFile===undefined){
            alert("No file uploaded !");
            return;
        }
        const fileReader = new FileReader();
        fileReader.onload = function(fileLoadedEvent){
            const text = fileLoadedEvent.target.result;
            if(text.length===0){
                alert("Text can not be empty ! Upload another file !");
                return;
            }
            let [encoded, treeStructure, info] = coder.encode(text);
            downloadFile(uploadedFile.name.split('.')[0] +'_encoded.txt', encoded);
            treearea.innerText = treeStructure;
            treearea.style.marginTop = '2000px';
            temptext.innerText = info;
        };
        fileReader.readAsText(uploadedFile, "UTF-8");
    };

    decode.onclick = function () {

        const uploadedFile = upload.files[0];
        if(uploadedFile===undefined){
            alert("No file uploaded !");
            return;
        }
        const fileReader = new FileReader();
        fileReader.onload = function(fileLoadedEvent){
            const text = fileLoadedEvent.target.result;
            if(text.length===0){
                alert("Text can not be empty ! Upload another file !");
                return;
            }
            let [decoded, treeStructure, info] = coder.decode(text);
            downloadFile(uploadedFile.name.split('.')[0] +'_decoded.txt', decoded);
            treearea.innerText = treeStructure;
            treearea.style.marginTop = '2000px';
            temptext.innerText = info;
        };
        fileReader.readAsText(uploadedFile, "UTF-8");
    };

};

function downloadFile(fileName, data){
    let downloadLink = document.createElement('a');
    downloadLink.href = "data:application/octet-stream,"+encodeURIComponent(data);
    downloadLink.download = fileName;
    downloadLink.click();
}