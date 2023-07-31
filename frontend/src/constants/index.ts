export const apiBaseUrl = 'http://localhost:8000/api/v1';

export const apiPaths = {
  newsletters: {
    list: `${apiBaseUrl}/newsletters/`,
    send: `${apiBaseUrl}/newsletters/send/`,
  }
};
