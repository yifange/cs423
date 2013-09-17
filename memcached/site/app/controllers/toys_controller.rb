class ToysController < ApplicationController
  def index
  end
  def show
    @key = params[:key]
    @value = Toy.find_by(:key => @key).value
  end
  def new
    @toy = Toy.new
  end
  def create
    toy = Toy.new(toy_params)
    if toy.save
      render :text => "success"
    else
      render :text => "fail"
    end
  end
  private
  def toy_params
    params.require(:toy).permit(:key, :value)
  end
end
