import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const marblesAPI = {
  getAll: (filters = {}) => api.get('/marbles', { params: filters }),
  getById: (id) => api.get(`/marbles/${id}`),
  create: (data) => api.post('/marbles', data),
  createBulk: (marbles) => api.post('/marbles/bulk', { marbles }),
  update: (id, data) => api.put(`/marbles/${id}`, data),
  delete: (id) => api.delete(`/marbles/${id}`),
};

export const artistsAPI = {
  getAll: () => api.get('/artists'),
  create: (data) => api.post('/artists', data),
};

export const stylesAPI = {
  getAll: () => api.get('/styles'),
};

export const vendorsAPI = {
  getAll: () => api.get('/vendors'),
  create: (data) => api.post('/vendors', data),
};

export const aiAPI = {
  identifyStyle: (imageData) => api.post('/identify-style', { image: imageData }),
};

export default api;
