document.getElementById("uploadForm").addEventListener("submit", async (e) => {

    e.preventDefault();

    const formData = new FormData(e.target);

    const response = await fetch("/upload", {
        method: "POST",
        body: formData
    });

    const data = await response.json();

    displayTable("inputTable", data.input);
    displayTable("outputTable", data.output);

});

function displayTable(id, rows){

    const table = document.getElementById(id);

    table.innerHTML = "";

    rows.forEach(row=>{

        const tr=document.createElement("tr");

        row.forEach(cell=>{

            const td=document.createElement("td");
            td.textContent=cell;
            tr.appendChild(td);

        });

        table.appendChild(tr);

    });

}