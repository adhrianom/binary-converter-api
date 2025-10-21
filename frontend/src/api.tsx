import axios from 'axios';

const api = axios.create({
  baseURL: 'https://binary-conversor-api.onrender.com',
});

export interface IEEE754Data {
  signal: number;
  exponent: string;
  mantissa: string;
}

export interface ConverterResponse {
  number_received: number;
  ieee754: IEEE754Data;
}

export async function convertToIEEE754(
  value: number
): Promise<ConverterResponse> {
  try {
    const response = await api.post<ConverterResponse>('/api/converter/', {
      number: value,
    });
    return response.data;
  } catch (error) {
    console.error('Error converting to IEEE754:', error);
    throw error;
  }
}
