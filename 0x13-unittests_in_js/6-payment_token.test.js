const getPaymentTokenFromAPI = require("./6-payment_token");
var { expect } = require("chai");

describe("getPaymentTokenFromAPI", function () {
  describe("async", function () {
    it("successful resolve", function (done) {
      getPaymentTokenFromAPI(true)
        .then((res) => {
          expect(res).to.include({data: "Successful response from the API"});
          done();
        })
        .catch((err) => done(err));
    });
  });
});
