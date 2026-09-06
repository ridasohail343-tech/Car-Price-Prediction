const button=document.querySelector(".predict");
button.addEventListener("click",async () => {
    const name=document.querySelector("#name").value;
    const company=document.querySelector("#company").value;
    const year=document.querySelector("#year").value;
    const km=document.querySelector("#km").value;
    const fuel=document.querySelector("#fuel").value;
    const response=await fetch("http://127.0.0.1:8000/predict",{
        method:"POST",
        headers:{
            "Content-type":"application/json"
        },
        body:JSON.stringify({
            name:name,
            company:company,
            year:Number(year),
            kms_driven:Number(km),
            fuel_type:fuel
        })
    });
    const data=await response.json();
    console.log(data);
    document.querySelector("#predicted_price").innerText=
    `Predicted_price:${data.predicted_price}`;
});



