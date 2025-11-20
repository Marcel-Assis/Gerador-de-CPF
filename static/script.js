function formatarCPF(cpf) {
    // Formata o CPF como XXX.XXX.XXX-XX
    return cpf.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, '$1.$2.$3-$4');
}

async function gerarCPF() {
    try {
        // Chama o endpoint da API.
        const response = await fetch('/cpf');
        const cpfString = await response.json(); // O resultado é uma string JSON
        
        const cpfFormatado = formatarCPF(cpfString);
        
        document.getElementById('cpf-display').textContent = cpfFormatado;
    } catch (error) {
        console.error('Erro ao buscar CPF:', error);
        document.getElementById('cpf-display').textContent = 'Erro ao carregar';
    }
}

// Gera um CPF na primeira carga da página
gerarCPF(); 