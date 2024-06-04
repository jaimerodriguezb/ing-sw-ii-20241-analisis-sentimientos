import useForm from "./UseForm";
import getConfig from "./Data"
import React, { useState } from "react";
import Select from "react-select";

const Form = () => {
    const { handleSubmit, status, Mensaje } = useForm();
    const {FORM_ENDPOINT} = getConfig();


    if (status === "success") {
        return (
            <>
                <div className="text-2xl">Gracias por utilizar el software</div>
                <div className="text-md">{Mensaje}</div>
            </>
        );
    }

    if (status === "error") {
        return (
            <>
                <div className="text-2xl">Hubo un error en la ejecuci&oacute;n</div>
                <div className="text-md">{Mensaje}</div>
            </>
        );
    }

    return (
        <form
            action={FORM_ENDPOINT}
            onSubmit={handleSubmit}
            method="GET"
        >   <div className="pt-0 mb-3">
                <h1>Tu sentimiento es</h1>
            </div>
            <div className="pt-0 mb-3">
                <input
                    type="text"
                    placeholder="Mensaje"
                    name="Mensaje"
                    className="focus:outline-none focus:ring relative w-full px-3 py-3 text-sm text-gray-600 placeholder-gray-400 bg-white border-0 rounded shadow outline-none"
                    required
                />
            </div>
          
            {status !== "loading" && (
                <div className="pt-0 mb-3">
                    <button
                        class="custom-button"
                        type="submit"
                    >
                        Calcular
                    </button>
                </div>
            )}
        </form>
    );
};

export default Form;
