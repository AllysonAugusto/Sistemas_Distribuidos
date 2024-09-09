package com.anchietaalbano.trabalho;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import static com.anchietaalbano.trabalho.Ticket.idManager;

public class Passagem {
    private final Map<String, Ticket> tickets = new HashMap<>();

    public String reservar_ticket(String cpf, String data, String hora, String origem, String destino, String nome, int poltrona) throws Exception {
        // Verifica se a poltrona já está reservada
        for (Ticket t : tickets.values()) {
            if (t.getPoltrona() == poltrona) {
                throw new Exception("Poltrona já reservada! Escolha outra!");
            }
        }
        // Verifica se o ônibus está cheio (por exemplo, se o número de tickets é maior que a capacidade)
        if (tickets.size() >= 20) { // Supondo que a capacidade do ônibus seja 20
            throw new Exception("Ônibus cheio");
        }

        // Cria e adiciona o ticket ao mapa
        Ticket novoTicket = new Ticket(cpf, data, hora, origem, destino, nome, poltrona);
        tickets.put(novoTicket.getId(), novoTicket);
        return novoTicket.getId();
    }

    public String atualizar_reserva(String ticketId, Ticket atualizacao) throws Exception {
        Ticket ticket = tickets.get(ticketId);

        if (ticket == null) {
            throw new Exception("Ticket não existe!");
        }

        idManager.liberarId(ticket.getId());

        String novoId = idManager.gerarId();

        atualizacao.setId(novoId);

        tickets.put(ticketId, atualizacao);
        return atualizacao.getId();
    }

    public String cancelar_reserva(String ticketId) throws Exception {
        Ticket ticket = tickets.remove(ticketId);

        if (ticket == null) {
            throw new Exception("ID do ticket inválido");
        }

        idManager.liberarId(ticketId);

        return "Ticket cancelado: " + ticketId;
    }

    public List<String> consultar_reserva(String cpf) throws Exception {
        List<String> resultado = new ArrayList<>();

        for (Ticket t : tickets.values()) {
            if (t.getCpf().equals(cpf)) {
                resultado.add(t.toString());
            }
        }

        if (resultado.isEmpty()) {
            throw new Exception("Não há tickets reservados para esse CPF.");
        }

        return resultado;
    }

    public boolean reservaExiste(String ticketId) {
        Ticket ticket = tickets.get(ticketId);
        return ticket != null; // Retorna true se o ticket existir, false caso contrário
    }

}
