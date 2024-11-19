import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  try {
    const photoResponse = await uploadPhoto();
    const userResponse = await createUser();

    return {
      photo: photoResponse,
      user: userResponse,
    };
  } catch (error) {
    // En cas d'erreur, retourner un objet avec des valeurs nulles
    return {
      photo: null,
      user: null,
    };
  }
}
