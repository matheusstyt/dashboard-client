let modal = document.getElementById('modal')
let dataFaturamento = document.getElementById('id_data_faturamento')

const today = new Date();
let dd = String(today.getDate())
if( dd.length < 2){
    dd = '0'+dd
}
let mm = today.getMonth()+1
let aaaa = today.getFullYear()
let dataFormatada = aaaa+'-'+mm+'-'+dd
dataFaturamento.value = dataFormatada
function sair(){
    modal.style.display = 'none';
}
function abrir(){
    modal.style.display = 'flex';
}
