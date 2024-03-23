import { uploadPhoto, createUser } from "./utils.js";

async function handleProfileSignup() {
  try {
    const [photo, user] = await Promise.all([uploadPhoto(), createUser()]);
    console.log(`${photo.body} ${user.firstName} ${user.lastName}`);
  } catch (error) {
    console.error("Signup system offline");
  }
}

export default handleProfileSignup;
