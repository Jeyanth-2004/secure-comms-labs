const zlib = require("zlib");
const list = ["eJzzyc9Lyc8DAAgpAms=", "eJxzSi3KycwDAAfXAl0=", "eJzzSy1XiMwvygYADKUC8A=="];
for (const s of list) console.log(s, "->", zlib.inflateSync(Buffer.from(s, "base64")).toString());
console.log("--- abc repeated vs random ---");
const rnd = n => { let r = ""; for (let i = 0; i < n; i++) r += String.fromCharCode(97 + Math.floor(Math.random() * 26)); return r; };
for (const k of [1, 5, 10, 50, 100]) {
  const a = "abc".repeat(k), b = rnd(a.length);
  console.log("input length", a.length, "| abc.. compressed:", zlib.deflateSync(a).toString("base64").length, "| random compressed:", zlib.deflateSync(b).toString("base64").length);
}
