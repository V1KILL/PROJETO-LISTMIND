
function AddMembro() {
    Swal.fire({
        title: '<p>Novo Cliente</p>',
        html: `
            <input id="name" class="swal2-input" placeholder="Nome" autocomplete="off">
            <textarea id="defect" class="swal2-textarea" placeholder="Defeito Relatado"></textarea>
            <div>
                <select id="option" class="swal2-select">
                    <option value="0">Serviço</option>
                    <option value="1">Diagnóstico</option>
                    <option value="2">Compra</option>
                </select>
            </div>
            <input class="swal2-input" type="date" id="predicted-date" name="predicted-date"><br><br>
            <input id="predicted-price" class="swal2-input" placeholder="Valor Previsto" type="number" autocomplete="off" required>
            <input id="price" class="swal2-input" placeholder="Valor Pago" type="number" autocomplete="off" required>
            <textarea id="service" class="swal2-textarea" placeholder="Serviço a Ser Executado"></textarea>
            <textarea id="part" class="swal2-textarea" placeholder="Peças Aplicadas"></textarea>
        `,
        
        confirmButtonText: 'Adicionar Cliente',
        cancelButtonText: 'Cancelar',
        confirmButtonColor: '#19C37D',
        cancelButtonColor: '#d33',
        
        showLoaderOnConfirm: true,
        showCancelButton: true,
        preConfirm: () => {
            const name = Swal.getPopup().querySelector('#name').value;
            const price = Swal.getPopup().querySelector('#price').value;
            const defect = Swal.getPopup().querySelector('#defect').value;
            const option = Swal.getPopup().querySelector('#option').value;
            const predicted_date = Swal.getPopup().querySelector('#predicted-date').value;
            const predicted_price = Swal.getPopup().querySelector('#predicted-price').value;
            const service = Swal.getPopup().querySelector('#service').value;
            const part = Swal.getPopup().querySelector('#part').value;

            if (!name || !price || !defect || !option || !predicted_date || !predicted_price || !service || !part) {
                Swal.showValidationMessage('Todos os campos são obrigatórios');
                return false;
            }

            
            window.location.href = `/addclient/${name}/${defect}/${option}/${predicted_date}/${predicted_price}/${price}/${service}/${part}`;
        },
        allowOutsideClick: () => !Swal.isLoading(),
    });
}



function Mudar(id, status, name, description) {
    
    let checkbox;
    let isChecked = 'False';
    if (status == 'True') {
        isChecked = 'checked';
    }
    Swal.fire({
        title: `${name}`,
        html:
           `<input id="nome" class="swal2-input" placeholder="Nome" autocomplete="off" value=${name}>
            <textarea id="descricao" class="swal2-textarea" placeholder="Descrição" >${description}</textarea>
                
            <div class="checkbox-container">
                <input id="feito" type="checkbox" class="swal2-checkbox" ${isChecked}>
                <label for="feito" class="swal2-checkbox-label">Feito</label>
                <div>
                    <a href="/clientdelete/${id}" id="excluir" class="swal2-a">Excluir Cliente</a>
                </div>
            </div>`,

        confirmButtonText: 'Editar',
        cancelButtonText: 'Cancelar',
        confirmButtonColor: '#19C37D',
        cancelButtonColor: '#d33',
        showCancelButton: true,
       

        preConfirm: () => {
            const nome = document.getElementById('nome').value;
            const descricao = document.getElementById('descricao').value;
            const checkbox = document.getElementById('feito').checked;

  
            
            if (!nome.trim() || !descricao.trim()) {
                Swal.showValidationMessage('O Título e a Descrição Não Podem Ser Vazios');
                return false;
              }

            return { nome: nome, descricao: descricao, checkbox: checkbox };
        },
        
    }).then(result => {
        if (result.isConfirmed) {
            const { nome, descricao, checkbox } = result.value;
            window.location.href = `/serviceedit/${checkbox}/${id}/${nome}/${descricao}`;
        }
    });
}

function Document(id){
    window.open(`/document/${id}`, '_blank');
}

var elementoFaturamento = document.getElementById('myChart');

var faturamentoMensalString = elementoFaturamento.dataset.faturamento;
var faturamentoMensal = JSON.parse(faturamentoMensalString);


var data = {
    labels: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
    datasets: [{
        label: 'Faturamento Mensagel',
        data: faturamentoMensal,
        backgroundColor: 'rgb(1,208,119, 0.2)',
        borderColor:'#01D077',
        borderWidth: 1
    }]
};


var options = {
    scales: {
        y: {
            beginAtZero: true
        }
    }
};


var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: data,
    options: options,
    
});