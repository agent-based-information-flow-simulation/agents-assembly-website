import { browser } from '$app/env';

export const getApiUrl = () => {
	return browser ? (import.meta.env.VITE_CLIENT_SIDE_API_URL) : (import.meta.env.VITE_SERVER_SIDE_API_URL);
};
