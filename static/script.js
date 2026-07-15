const uploadBtn = document.getElementById("uploadBtn");

const pdf = document.getElementById("pdf");

const spinner = document.getElementById("spinner");

const status = document.getElementById("status");

const downloadBtn = document.getElementById("downloadBtn");

const messages = [

    "Uploading PDF...",

    "Extracting text...",

    "Reading tables...",

    "Generating Markdown...",

    "Almost done..."

];

let interval;


uploadBtn.onclick = async () => {

    if(pdf.files.length===0){

        alert("Choose a PDF first.");

        return;

    }

    uploadBtn.disabled=true;

    spinner.style.display="block";

    let i=0;

    status.innerText=messages[0];

    interval=setInterval(()=>{

        i=(i+1)%messages.length;

        status.innerText=messages[i];

    },1500);

    const formData=new FormData();

    formData.append("file",pdf.files[0]);

    try{

        const response=await fetch("/upload",{

            method:"POST",

            body:formData

        });

        const data=await response.json();

        clearInterval(interval);

        spinner.style.display="none";

        status.innerText="✔ Parsing Complete!";

        downloadBtn.href="/download/"+data.filename;

        downloadBtn.classList.remove("hidden");

    }

    catch(err){

        clearInterval(interval);

        spinner.style.display="none";

        status.innerText="Something went wrong.";

    }

    uploadBtn.disabled=false;

}