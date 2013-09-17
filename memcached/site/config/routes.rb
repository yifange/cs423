Site::Application.routes.draw do
  get "toys/new" => "toys#new"
  get "toys/show/:key" => "toys#show"
  post "toys" => "toys#create"
end
