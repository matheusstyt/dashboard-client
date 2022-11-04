// tratamento de data 
let dataFaturamento = document.getElementById('id_data_faturamento')
const today = new Date();
let dd = String(today.getDate())
if( dd.length < 2){
    dd = '0'+dd
}
let mm = today.getMonth()+1
let aaaa = today.getFullYear()

dataFaturamento.value = String(aaaa+'-'+mm+'-'+dd)

// modal de adiçaõ
let modal = document.getElementById('modal')
function sair(){
    modal.style.display = 'none';
}
function abrir(){
    modal.style.display = 'flex';
}
// // modal de edição
// let modalEdit = document.getElementById('modalEdit')
// function sairEdit(){
//     modalEdit.style.display = 'none';
// }
// function abrirEdit(){
//     modalEdit.style.display = 'flex';
// }

// MODAL DE IMPLATAÇÃO 

function sair1(){
    document.getElementById('modal1').style.display = 'none';
}
function abrir1(){
    document.getElementById('modal1').style.display = 'flex';

}
function sair2(){
    document.getElementById('modal2').style.display = 'none';
}
function abrir2(){
    document.getElementById('modal2').style.display = 'flex';
}

function sair3(){
    document.getElementById('modal3').style.display = 'none';
}
function abrir3(){
    document.getElementById('modal3').style.display  = 'flex';
}

const myObject = document.getElementById('id_descricao_planejado');
myObject.addEventListener('keydown', function (evt) {
// your code goes here 
 console.log(myObject.value);
});
myObject.value = 'testea'