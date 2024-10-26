import axios from 'axios';

export const calculateNPI = async(expression) => {
    try {
        const response = await axios.post('http://localhost:8000/calculate', { expression });
        return response.data.result;
    } catch (error) {
        console.error("Erreur dans l'appel API :", error);
        throw error;
    }
};