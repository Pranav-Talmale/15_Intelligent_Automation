import mongoose from "mongoose";
import dotenv from "dotenv";

dotenv.config();

export const dbConnect = () => {
  mongoose.connection.once("open", () => console.log("DB connection"));
  return mongoose.connect(
    "mongodb+srv://pranav:12345@cluster0.2en0uzc.mongodb.net/",
    { keepAlive: true }
  );
};
