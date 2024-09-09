package com.anchietaalbano.trabalho;

import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;

import java.nio.charset.StandardCharsets;
import java.util.logging.Logger;

public class Despachante {
    private final Esqueleto esqueleto;
    private static final Gson gson = new Gson();
    private static final Logger logger = Logger.getLogger(Despachante.class.getName());

    public Despachante() {
        this.esqueleto = new Esqueleto();
    }

    public String invoke(String request) {

        try {
            logger.info("Recebendo requisição: " + request);

            JsonObject json = JsonParser.parseString(request).getAsJsonObject();
            String metodo = json.get("methodId").getAsString();
            JsonObject params = json.get("arguments").getAsJsonObject();

            String result;
            int status;
            switch (metodo) {
                case "reservar_ticket":
                    logger.info("Invocando método: reservar_ticket");
                    result = esqueleto.reservar_ticket(params);
                    status = 201; // Created
                    break;
                case "atualizar_reserva":
                    logger.info("Invocando método: atualizar_ticket");
                    result = esqueleto.atualizar_reserva(params);
                    status = 200; // OK
                    break;
                case "cancelar_reserva":
                    logger.info("Invocando método: cancelar_reserva");
                    result = esqueleto.cancelar_reserva(params);
                    status = 200; // OK
                    break;
                case "consultar_reserva":
                    logger.info("Invocando método: consultar_reserva");
                    result = esqueleto.consultar_reserva(params);
                    status = 200; // OK
                    break;
                default:
                    result = "Erro: Método não encontrado";
                    status = 404; // Not Found
                    logger.severe("Método não encontrado: " + metodo);
                    break;
            }

            JsonObject response = new JsonObject();
            response.addProperty("messageType", 1);
            response.addProperty("requestId", json.get("requestId").getAsInt());
            response.addProperty("methodId", metodo);
            response.addProperty("status", status);


            JsonArray responseArray = new JsonArray();
            responseArray.add(result);
            response.add("arguments", responseArray);

            logger.info("Resposta gerada: " + response);
            return gson.toJson(response);

        } catch (Exception e) {
            logger.severe("Erro ao processar a requisição:  " + e.getMessage());
            return "Erro: " + e.getMessage();
        }
    }
}
