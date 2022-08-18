const sendPaymentRequestToApi = require("./3-payment");
const sinon = require("sinon");
let { expect } = require("chai");
const Utils = require("./utils");

describe("calculateNumber", function () {
  it("has correct math", () => {
    const stubUtils = sinon.stub(Utils, "calculateNumber");
    stubUtils.returns(10);
    const spyConsole = sinon.stub(console, "log");

    sendPaymentRequestToApi(100, 20);

    expect(stubUtils.calledOnceWithExactly("SUM", 100, 20)).to.be.true;
    expect(spyConsole.calledOnceWithExactly("The total is: 10")).to.be.true;

    stubUtils.restore();
    spyConsole.restore();
  });
});
